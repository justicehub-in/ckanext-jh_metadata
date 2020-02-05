import ckan.plugins as p
import ckan.plugins.toolkit as tk


class Jh_MetadataPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):

    # with IDatasetForm plugin interface,
    # a CKAN plugin can add custom, first-class metadata fields to CKAN datasets,
    # and can do custom validation of these fields.
    p.implements(p.IDatasetForm)

    # This interface allows to implement a function update_config()
    # that allows us to update the CKAN config,
    # in our case we want to add an additional location for CKAN to look for templates.
    p.implements(p.IConfigurer)

    def update_config(self, config_):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config_, 'templates')

        tk.add_public_directory(config_, 'public')
        tk.add_resource('fanstatic', 'jh_metadata')

    def _modify_package_schema(self, schema):
        schema.update({
            'custom_text': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        return schema

    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(Jh_MetadataPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(Jh_MetadataPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(Jh_MetadataPlugin, self).show_package_schema()

        schema.update({
            'custom_text': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
