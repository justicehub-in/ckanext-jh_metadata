import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Jh_SearchfacetsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'jh_searchfacets')

    def dataset_facets(self,facets_dict, package_type):
        facets_dict['groups'] = plugins.toolkit._('Sectors')
        facets_dict['organization'] = plugins.toolkit._('Partners')
        facets_dict['states'] = plugins.toolkit._('Geography: States')
        return  facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        facets_dict['groups'] = plugins.toolkit._('Sectors')
        facets_dict['organization'] = plugins.toolkit._('Partners')
        facets_dict['states'] = plugins.toolkit._('Geography: States')
        return  facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        facets_dict['groups'] = plugins.toolkit._('Sectors')
        facets_dict['organization'] = plugins.toolkit._('Partners')
        facets_dict['states'] = plugins.toolkit._('Geography: States')
        return facets_dict
