<<<<<<< HEAD
<<<<<<< HEAD


=======
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
>>>>>>> 97dea7d924258b36c600a4fd74bc6f9d1fad8ffb
=======


>>>>>>> 0214c3b7ba82f5d9d29e2288e8e03d04bfcc5c0f
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoFinal.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
<<<<<<< HEAD
<<<<<<< HEAD
    main()

    
=======
    main()
>>>>>>> 97dea7d924258b36c600a4fd74bc6f9d1fad8ffb
=======
    main()

    
>>>>>>> 0214c3b7ba82f5d9d29e2288e8e03d04bfcc5c0f
