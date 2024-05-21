import json

def get_articles():
    with open('articles.json', 'r', encoding='utf-8') as file:
        articles = json.load(file)
    return articles


def save_article(name, text):
    with open('articles.json', 'r', encoding='utf-8') as file:
        articles = json.load(file)
        articles[name] = text
    with open('articles.json', 'w', encoding='utf-8') as file:
        json.dump(articles, file, ensure_ascii=False)



def delete_article(name):
    with open('articles.json', 'r', encoding='utf-8') as file:
        article = json.load(file)
        del article[name]
    with open('articles.json', 'w', encoding='utf-8') as file:
        json.dump(article, file, ensure_ascii=False)


def main():
    print(get_articles())
    print(save_article('Да', 'Нет'))
    delete_article('Да')

if __name__ == '__main__':
    main()
