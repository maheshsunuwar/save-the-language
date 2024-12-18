import reflex as rx

from rxconfig import config

class AppConfig(rx.Config):
    pass

config = AppConfig(
    app_name = 'Save The Language Foundation',
    tailwind={
        'theme':{
        },
        'plugins': ['@tailwindcss/typography']
    }
)

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(
                "Save The Language Foundation", 
                size="9",
                _hover = {
                    # 'color':'green'
                },
            ),
            rx.text(
                "Coming Soon...",
                size="5",
            ),
            
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

app = rx.App(
    style={
        # 'background':'blue',
        # 'color':'white'
    }
)
app.add_page(index)
