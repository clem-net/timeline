import wikipedia


def main():
    for i in range(0, 999):
        try:
            if i % 10 == 0:
                continue
            page = wikipedia.page(pageid=i)
            validatePage(page)
            # print(i, " ", page.url)
        except wikipedia.exceptions.PageError as e:
            pass
        except wikipedia.exceptions.DisambiguationError as e:
            pass


# Attribute page is a wikipedia page
def validatePage(page):
    # Validate unless page is
    # a talk page
    # a list
    split = "/wiki/"
    urlTitle = page.url.split(split)[1]
    if urlTitle.startswith("Talk:"):
        print(urlTitle)
        return False
    elif urlTitle.startswith("List"):
        print(urlTitle)
        return False
    else:
        return true


if __name__ == "__main__":
    main()
