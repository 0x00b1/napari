from napari.editor.setting import Setting


class SettingController:
    def __init__(self):
        pass

    @staticmethod
    def create(name: str, required: bool) -> 'Setting':
        return Setting(name, required)

    @staticmethod
    def update_data(setting: 'Setting', data: any) -> 'Setting':
        setting.data = data

        return setting

    @staticmethod
    def update_name(setting: 'Setting', name: str) -> 'Setting':
        setting.name = name

        return setting
