import wikipedia


def main():
    for i in range(30, 999):
        try:
            if i % 10 == 0:
                continue
            page = wikipedia.page(pageid=i)
            print(i, " ", page.url)
        except wikipedia.exceptions.PageError as e:
            print(str(e))
            # pass
        except wikipedia.exceptions.DisambiguationError as e:
            print(str(e))


if __name__ == "__main__":
    main()
