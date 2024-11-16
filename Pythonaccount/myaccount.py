from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivy.uix.filechooser import FileChooserListView
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
import re
from kivymd.uix.dialog import MDDialog
import os

KV = '''
ScreenManager:
    MainScreen:
    EditProfileScreen:

<MainScreen>:
    name: "main"

    MDBoxLayout:
        orientation: "vertical"
        padding: [15, 20, 15, 15]
        spacing: "10dp"

        MDTopAppBar:
            title: "Profile"
            left_action_items: [['arrow-left', lambda x: app.back_action()]]

        MDBoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: "200dp"
            spacing: "10dp"
            pos_hint: {"center_x": 0.5}

            Image:
                id: profile_image
                source: "unnamed (1).png"
                size_hint: None, None
                size: "120dp", "120dp"
                pos_hint: {"center_x": 0.5}

            MDIconButton:
                icon: "camera"
                user_font_size: "24sp"
                pos_hint: {"center_x": 0.5}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_release: app.change_avatar()

        MDLabel:
            id: name_label
            text: "Name: Melissa Peters"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: "40dp"

        MDLabel:
            id: dob_label
            text: "Date of Birth: 23/05/1995"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: "40dp"

        MDLabel:
            id: country_label
            text: "Country: Nigeria"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: "40dp"

        MDLabel:
            id: email_label
            text: "Email: melpeters@gmail.com"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: "40dp"

        MDLabel:
            id: password_label
            text: "Password: ************"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: "40dp"

        MDRaisedButton:
            text: "Edit Profile"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            on_release: app.switch_to_edit_profile()

<EditProfileScreen>:
    name: "edit_profile"

    MDBoxLayout:
        orientation: "vertical"
        padding: [15, 20, 15, 150]
        spacing: "10dp"

        MDTopAppBar:
            title: "Edit Profile"
            left_action_items: [['arrow-left', lambda x: app.back_to_main()]]

        MDTextField:
            id: name_field
            hint_text: "Name"
            text: "Melissa Peters"
            mode: "rectangle"
            size_hint_y: None

        MDTextField:
            id: dob_field
            hint_text: "Date of Birth"
            text: "23/05/1995"
            mode: "rectangle"
            size_hint_y: None

        MDTextField:
            id: country_field
            hint_text: "Country"
            text: "Nigeria"
            mode: "rectangle"
            size_hint_y: None
            on_focus: app.show_country_menu(self)

        MDTextField:
            id: email_field
            hint_text: "Email"
            text: "melpeters@gmail.com"
            mode: "rectangle"
            size_hint_y: None

        MDTextField:
            id: password_field
            hint_text: "Password"
            password: True
            text: "************"
            mode: "rectangle"
            size_hint_y: None

        MDIconButton:
            id: password_eye_icon
            icon: "eye-off"
            pos_hint: {"center_x": 0.5}
            on_release: app.toggle_password_visibility()

        MDRaisedButton:
            text: "Save changes"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            on_release: app.save_changes()
'''

class MainScreen(Screen):
    pass

class EditProfileScreen(Screen):
    pass

class ProfileApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def back_action(self):
        pass

    def change_avatar(self):
        try:
            file_chooser = FileChooserListView()
            file_chooser.filters = ['*.png', '*.jpg', '*.jpeg']  # Filter to only show images
            file_chooser.bind(on_selection=self.load_image)

            # Define the cancel button
            cancel_button = MDRaisedButton(
                text="Cancel",
                size_hint=(None, None),
                size=("120dp", "40dp"),
                pos_hint={"center_x": 0.5},
                on_release=self.close_dialog
            )

            # Create the dialog with the file chooser and cancel button
            self.dialog = MDDialog(
                title="Choose a new avatar",
                type="custom",
                content_cls=file_chooser,
                size_hint=(0.8, 0.8),
                buttons=[cancel_button]
            )
            self.dialog.open()
        except Exception as e:
            print(f"Error opening file chooser: {e}")

    def close_dialog(self, instance):
        self.dialog.dismiss()

    def load_image(self, instance, value):
        if value:
            try:
                selected_image = value[0]
                print(f"Selected file: {selected_image}")

                if os.path.exists(selected_image):
                    self.root.ids.profile_image.source = selected_image
                    self.dialog.dismiss()
                else:
                    print("File does not exist.")
            except Exception as e:
                print(f"Error loading image: {e}")
                self.dialog.dismiss()
        else:
            print("No file selected.")

    def switch_to_edit_profile(self):
        self.root.current = "edit_profile"

    def back_to_main(self):
        self.root.current = "main"

    def show_country_menu(self, instance):
        countries = [
            "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
            "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
            "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
            "Bulgaria",
            "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
            "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)",
            "Congo (Democratic Republic of the)",
            "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic (Czechia)", "Denmark", "Djibouti", "Dominica",
            "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
            "Eswatini",
            "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece",
            "Grenada",
            "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India",
            "Indonesia",
            "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan",
            "Kenya",
            "Kiribati", "Korea (North)", "Korea (South)", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
            "Lesotho",
            "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
            "Maldives",
            "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
            "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
            "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
            "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania",
            "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
            "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone",
            "Singapore",
            "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka",
            "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
            "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu",
            "Uganda",
            "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
            "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
        ]
        menu_items = [{"viewclass": "OneLineListItem", "text": country, "on_release": lambda x=country: self.set_country(instance, x)} for country in countries]
        self.menu = MDDropdownMenu(caller=instance, items=menu_items, width_mult=4)
        self.menu.open()

    def set_country(self, instance, country):
        instance.text = country
        self.menu.dismiss()

    def toggle_password_visibility(self):
        password_field = self.root.get_screen("edit_profile").ids.password_field
        password_eye_icon = self.root.get_screen("edit_profile").ids.password_eye_icon


        if password_field.password:
            password_field.password = False
            password_eye_icon.icon = "eye"
        else:
            password_field.password = True
            password_eye_icon.icon = "eye-off"

    def save_changes(self):
        edit_screen = self.root.get_screen("edit_profile")
        name = edit_screen.ids.name_field.text
        dob = edit_screen.ids.dob_field.text
        country = edit_screen.ids.country_field.text
        email = edit_screen.ids.email_field.text
        password = edit_screen.ids.password_field.text


        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            self.dialog = MDDialog(
                title="Invalid Email",
                text="Please enter a valid email address.",
                buttons=[MDRectangleFlatButton(text="OK", on_release=self.dismiss_invalid_email)]
            )
            self.dialog.open()
            return


        main_screen = self.root.get_screen("main")
        main_screen.ids.name_label.text = f"Name: {name}"
        main_screen.ids.dob_label.text = f"Date of Birth: {dob}"
        main_screen.ids.country_label.text = f"Country: {country}"
        main_screen.ids.email_label.text = f"Email: {email}"
        main_screen.ids.password_label.text = "Password: ************"

        self.root.current = "main"

    def dismiss_invalid_email(self, instance):
        self.dialog.dismiss()

if __name__ == "__main__":
    ProfileApp().run()