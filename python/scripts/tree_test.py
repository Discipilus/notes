#!/usr/bin/env python

from pprint import pprint
from collections import deque


TEST_TREE = {
    'name': 'root',
    'value': 0,
    'children': [
        {
            'name': 'child1',
            'value': 1,
            'children': [
                {
                    'name': 'child11',
                    'value': 11,
                    'children': [
                        {
                            'name': 'child111',
                            'value': 111,
                            'children': []
                        },
                        {
                            'name': 'child112',
                            'value': 112,
                            'children': []
                        },
                        {
                            'name': 'child113',
                            'value': 113,
                            'children': []
                        },
                    ]
                },
                {
                    'name': 'child12',
                    'value': 12,
                    'children': [
                        {
                            'name': 'child121',
                            'value': 121,
                            'children': []
                        },
                        {
                            'name': 'child122',
                            'value': 122,
                            'children': []
                        },
                        {
                            'name': 'child123',
                            'value': 123,
                            'children': []
                        },
                    ]
                },
                {
                    'name': 'child13',
                    'value': 13,
                    'children': [
                        {
                            'name': 'child131',
                            'value': 131,
                            'children': []
                        },
                        {
                            'name': 'child132',
                            'value': 132,
                            'children': []
                        },
                        {
                            'name': 'child133',
                            'value': 133,
                            'children': []
                        },
                    ]
                },
            ]
        },
        {
            'name': 'child2',
            'value': 2,
            'children': [
                {
                    'name': 'child21',
                    'value': 21,
                    'children': [
                        {
                            'name': 'child211',
                            'value': 211,
                            'children': []
                        },
                        {
                            'name': 'child212',
                            'value': 212,
                            'children': []
                        },
                        {
                            'name': 'child213',
                            'value': 213,
                            'children': []
                        },
                    ]
                },
                {
                    'name': 'child22',
                    'value': 22,
                    'children': [
                        {
                            'name': 'child221',
                            'value': 221,
                            'children': []
                        },
                        {
                            'name': 'child222',
                            'value': 222,
                            'children': []
                        },
                        {
                            'name': 'child223',
                            'value': 223,
                            'children': []
                        },
                    ]
                },
                {
                    'name': 'child23',
                    'value': 23,
                    'children': [
                        {
                            'name': 'child231',
                            'value': 231,
                            'children': []
                        },
                        {
                            'name': 'child232',
                            'value': 232,
                            'children': []
                        },
                        {
                            'name': 'child233',
                            'value': 233,
                            'children': []
                        },
                    ]
                },
            ]
        },
        {
            'name': 'child3',
            'value': 3,
            'children': [
                {
                    'name': 'child31',
                    'value': 31,
                    'children': [
                        {
                            'name': 'child311',
                            'value': 311,
                            'children': []
                        },
                        {
                            'name': 'child312',
                            'value': 312,
                            'children': []
                        },
                        {
                            'name': 'child313',
                            'value': 313,
                            'children': []
                        },
                    ]
                },
                {
                    'name': 'child32',
                    'value': 32,
                    'children': [
                        {
                            'name': 'child321',
                            'value': 321,
                            'children': []
                        },
                        {
                            'name': 'child322',
                            'value': 322,
                            'children': []
                        },
                        {
                            'name': 'child323',
                            'value': 323,
                            'children': []
                        },
                    ]
                },
                {
                    'name': 'child33',
                    'value': 33,
                    'children': [
                        {
                            'name': 'child331',
                            'value': 331,
                            'children': []
                        },
                        {
                            'name': 'child332',
                            'value': 332,
                            'children': []
                        },
                        {
                            'name': 'child333',
                            'value': 333,
                            'children': []
                        },
                    ]
                },
            ]
        },
    ]
}


def get_plain_data_recursive(node: dict, parent: str = '') -> list[dict]:
    plain_data = []
    name = f"{parent}.{node.get('name')}" if parent else node.get('name')
    value = node.get('value')
    plain_data.append({name: value})
    for child in node.get('children'):
        data = get_plain_data_recursive(child, name)
        plain_data.extend(data)
    return plain_data


def get_plain_data_non_recursive(node: dict) -> list[dict]:
    plain_data = []
    name = node.get('name')
    value = node.get('value')
    plain_data.append({name: value})
    children = deque(node.get('children'))
    parent_name = name
    while len(children):
        ### First top levels then bottom ones
        ### current = children.popleft()
        
        ### Branch by branch
        current = children.pop()
        full_child_name = f'{parent_name}.{current.get("name")}'
        plain_data.append({full_child_name: current.get('value')})
        for child in current.get('children'):
            child['name'] = f'{current.get("name")}.{child.get("name")}'
            children.append(child)
    return plain_data


def main():
    plain_data1 = get_plain_data_recursive(TEST_TREE)
    pprint(plain_data1)
    plain_data2 = get_plain_data_non_recursive(TEST_TREE)
    pprint(plain_data2)
    assert sorted(plain_data1, key=lambda x: ''.join(x.keys())) == sorted(plain_data2, key=lambda x: ''.join(x.keys()))


if __name__ == '__main__':
    main()
