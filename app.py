#!/usr/bin/env python3

import datetime
import logging

import connexion
from connexion import NoContent

import orm

import pandas as pd


db_session = None


# Users
def get_users(limit, user_type=None):
    q = db_session.query(orm.User)
    if user_type:
        q = q.filter(orm.User.user_type == user_type)
    return [p.dump() for p in q][:limit]


def get_user(user_id):
    user = db_session.query(orm.User).filter(orm.User.id == user_id).one_or_none()
    return user.dump() if user is not None else ('Not found', 404)


def put_user(user_id, user):
    p = db_session.query(orm.User).filter(orm.User.id == user_id).one_or_none()
    user['id'] = user_id
    if p is not None:
        logging.info('Updating user %s..', user_id)
        p.update(**user)
    else:
        logging.info('Creating user %s..', user_id)
        user['created'] = datetime.datetime.utcnow()
        db_session.add(orm.User(**user))
    db_session.commit()
    return NoContent, (200 if p is not None else 201)


def delete_user(user_id):
    user = db_session.query(orm.User).filter(orm.User.id == user_id).one_or_none()
    if user is not None:
        logging.info('Deleting user %s..', user_id)
        db_session.query(orm.User).filter(orm.User.id == user_id).delete()
        db_session.commit()
        return NoContent, 204
    else:
        return NoContent, 404


# Datasets
def get_datasets(limit, dataset_type=None):
    q = db_session.query(orm.Dataset)
    if dataset_type:
        q = q.filter(orm.Dataset.dataset_type == dataset_type)
    return [p.dump() for p in q][:limit]


def get_dataset(dataset_id):
    dataset = db_session.query(orm.Dataset).filter(orm.Dataset.id == dataset_id).one_or_none()
    return dataset.dump() if dataset is not None else ('Not found', 404)


def put_dataset(dataset_id, dataset):
    p = db_session.query(orm.Dataset).filter(orm.Dataset.id == dataset_id).one_or_none()
    dataset['id'] = dataset_id
    if p is not None:
        logging.info('Updating dataset %s..', dataset_id)
        p.update(**dataset)
    else:
        logging.info('Creating dataset %s..', dataset_id)
        dataset['created'] = datetime.datetime.utcnow()
        db_session.add(orm.Dataset(**dataset))
    db_session.commit()
    return NoContent, (200 if p is not None else 201)


def delete_dataset(dataset_id):
    dataset = db_session.query(orm.Dataset).filter(orm.Dataset.id == dataset_id).one_or_none()
    if dataset is not None:
        logging.info('Deleting dataset %s..', dataset_id)
        db_session.query(orm.Dataset).filter(orm.Dataset.id == dataset_id).delete()
        db_session.commit()
        return NoContent, 204
    else:
        return NoContent, 404


def post_upload(upfile):
    # dataset = db_session.query(orm.Dataset).filter(orm.Dataset.id == dataset_id).one_or_none()
    print(upfile)
    dataset = pd.read_csv(upfile)
    print(dataset.head(10))
    print(dataset.describe())    
    # dataset_id = XXX
    if dataset is not None:
        # # logging.info('Uploading a dataset %s..', dataset_id)
        # db_session.add(orm.Dataset(**dataset))
        # db_session.commit()
        return NoContent, 202
    else:
        return NoContent, 404




logging.basicConfig(level=logging.INFO)
# db_session = orm.init_db('sqlite:///:memory:')
db_session = orm.init_db('postgresql://spock:spock@localhost:5432/spock')

app = connexion.FlaskApp(__name__)
app.add_api('spock_api.yaml')

application = app.app


@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(
        port=5000,
        threaded=True  # in-memory database isn't shared across threads
    )
