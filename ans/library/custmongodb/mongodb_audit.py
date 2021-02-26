#!/usr/bin/python

# Copyright: (c) 2020, Your Name <YourName@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: mongodb_audit

short_description: mongodb audit module

version_added: "1.0.0"

description: ongoing work to create the best mongodb auditing module

options:
    socketofmdb:
        description: This is the IP address and port of the mongodb
        required: true
        type: str

author:
    - Russell Zachary Feeser (@rzfeeser)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  mongodb_audit:
    ipofmdb: 127.0.0.1
    portofmdb: 27017
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
ipofmdb:
    description: The ip used to access the db
    type: str
    returned: always
    sample: 127.0.0.1
portofmdb:
    description: The port used to access the db
    type: str
    returned: always
    sample: 27017
mdb_results:
    description: Output from the MongoDB we connected to
    type: str
    returned: always
    sample: (will be json)
'''
from pymongo import MongoClient

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        ipofmdb=dict(type='str', required=True),
        portofmdb=dict(type='str', required=True),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        socketofmdb='',
        ipofmdb='',
        portofmdb='',
        mdb_results='',
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    mdbconn = f"mongodb://{module.params.get('ipofmdb')}:{module.params.get('portofmdb')}/"

    # this is JSON result we want to return
    result['socketofmdb'] = mdbconn
    result['ipofmdb'] = module.params.get('ipofmdb')
    result['portofmdb'] = module.params.get('portofmdb')

    # this is the "work" we want to do. Start connecting to MongoDB
    client = MongoClient( mdbconn )
    db=client.admin
    # Issue the serverStatus command and print the results
    serverStatusResult=db.command("serverStatus")
    
    # set our results in the JSON we return to Ansible
    result['mdb_results'] = str(serverStatusResult)
    
    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()


if __name__ == '__main__':
    main()
