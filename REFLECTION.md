#Reflection Questions

#Reflection Questions

1. I am using 

        "def test_page_shows_both_status_labels(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Completed")
        self.assertContains(response, "In progress")"

        This tests for these specific strings in the html files. Turns out these strings are case sensitive. One of the errors I got was "In progress" I had typed "In Progress". It returned an error because of the capital "P".

2. Using base.html and adding a page, I would only have to edit one page. Had I not used that, I would end up editing four files. Each of the four pages. So each page would have it's own specific version of the nav bar instead of sharing the one from base.html.
