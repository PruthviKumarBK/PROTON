__author__ = "Pruthvi Kumar, pruthvikumar.123@gmail.com"
__copyright__ = "Copyright (C) 2018 Pruthvi Kumar | http://www.apricity.co.in"
__license__ = "Public Domain"
__version__ = "1.0"

from jinja2 import Environment, FileSystemLoader
from nucleus.db.cache_manager import CacheManager


class ExecGen(CacheManager):
    """
    Execution files generator for PROTON stack.
    """

    def __init__(self):
        super(ExecGen, self).__init__()
        self.logger = self.get_logger(log_file_name='execGen_logs',
                                      log_file_path='{}/trace/execGen_logs.log'.format(self.ROOT_DIR))
        self.__jinja_env = Environment(loader=FileSystemLoader('{}/nucleus/templates/'.format(self.ROOT_DIR)))
        self.__iface_controllers_root = '{}/mic/iface/controllers'.format(self.ROOT_DIR)
        self.__iface_controllers_template = self.__jinja_env.get_template('iface_controller_template.py')
        self.__executor_template = self.__jinja_env.get_template('executor_template.py')

        self.generate_executor = self.__generate_executor

    def __generate_executor(self, port):
        """

        :return:
        """
        try:

            # Generate API layer based on methods available within generated controller.
            # 1. generate istore from methodExtractorTemplate for current micStack (i_method_fetch.py)
            # 2. from iextractor (which inherits from i_method_fetch.py), get all keys from current controller
            # for current micStack
            from nucleus.iextractorgen import IextractorGen
            ieg = IextractorGen()
            ieg.i_extractor()

            # Generate INTERFACE layer & Generate MAIN from all methods available for each controller in MIC Stack.
            from nucleus.iextractor import IExtractor
            iface_controllers = []
            routes = []
            iface_methods_in_proton_stack = IExtractor().keys_per_controller_in_proton_stack

            for mic_stacks in iface_methods_in_proton_stack:
                iface_controller_methods_hash = []
                for mic in mic_stacks:
                    for ix, method in enumerate(mic_stacks[mic]['restMethodsPerExposedMethod']):
                        iface_controller_methods_hash.append({'fileName': mic_stacks[mic]['fileName'],
                                                              'micName': mic_stacks[mic]['micName'],
                                                              'controllerName': mic_stacks[mic]['controllerName'],
                                                              'iControllerName': method,
                                                              'exposedRESTmethods': mic_stacks[mic]['restMethodsPerExposedMethod'][ix][method].keys()})

                        for method_type in mic_stacks[mic]['restMethodsPerExposedMethod'][ix][method]:
                            method_controller_name = 'Ictrl_'+method_type+'_' + mic_stacks[mic]['micName'] + '_' + method[method_type]
                            iface_controllers.append({'fileName': 'iface_ctrl_' + mic_stacks[mic]['micName'],
                                                      'controllerName': method_controller_name})
                            routes.append({'controllerName': method_controller_name,
                                           'routeName': method_type+'_{}_{}'.format(mic, method)})

                for mic in mic_stacks:
                    # Generate Interface Controller. The I of MIC stack per mic entry in PROTON stack.
                    with open(self.__iface_controllers_root + '/iface_ctrl_{}.py'.format(mic), 'w+') as icf:
                        icf.write(self.__iface_controllers_template.render(iCtrlHash=iface_controller_methods_hash))

            # Generate MAIN
            with open('{}/main.py'.format(self.ROOT_DIR), 'w+') as mf:
                mf.write(self.__executor_template.render(ifaceControllers=iface_controllers, routes=routes, port=port))

        except Exception as e:
            self.logger.exception('[ExecGen] - Exception while generating MAIN for {} MIC stack. '
                                  'Details: {}'.format(self.ROOT_DIR, str(e)))
