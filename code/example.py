from datadog import initialize, api
import datadog_api_client



options = {

    'api_key': '',

    'app_key': ''

}



initialize(**options)



title = 'Average Memory Free Shell'

widgets = [{

    'definition': {

        'type': 'timeseries',

        'requests': [

            {'q': 'avg:system.mem.free{*}'}

        ],

        'title': 'Average Memory Free'

    }

}]

layout_type = 'ordered'

description = 'A dashboard with memory info.'

is_read_only = True

notify_list = ['user@domain.com']

template_variables = [{

    'name': 'host1',

    'prefix': 'host',

    'default': 'my-host'

}]



saved_views = [{

    'name': 'Saved views for hostname 2',

    'template_variables': [{'name': 'host', 'value': '<HOSTNAME_2>'}]}

]



api.Dashboard.create(title=title,

                     widgets=widgets,

                     layout_type=layout_type,

                     description=description,

                     is_read_only=is_read_only,

                     notify_list=notify_list,

                     template_variables=template_variables,

                     template_variable_presets=saved_view)
