from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:

        model = Blog

        fields = [
            "title",
            "content",
        ]

        widgets = {

            "title": forms.TextInput(

                attrs={

                    "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",

                    "placeholder": "Enter Blog Title"

                }

            ),

            "content": forms.Textarea(

                attrs={

                    "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",

                    "placeholder": "Write your blog here...",

                    "rows": 8

                }

            )

        }

        labels = {

            "title": "Blog Title",

            "content": "Blog Content"

        }

        