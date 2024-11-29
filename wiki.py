import wikipediaapi

def fetch_wikipedia_summary(word, file_name="wikipedia_summary.txt"):
    wiki_wiki = wikipediaapi.Wikipedia('Wikipedia Summarizer (baldeeppal2004@gmail.comindia)','en')  
    page = wiki_wiki.page(word)

   
    if page.exists():
        summary = page.summary  
        
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"Title: {page.title}\n\n{summary}")
        print(f"Summary saved to '{file_name}'.")

        print("\nContent of the created file:")
        print("-" * 40)
        with open(file_name, "r", encoding="utf-8") as file:
            print(file.read())
    else:
        print(f"The page for '{word}' does not exist on Wikipedia.")

if __name__ == "__main__":
    
    word = input("Enter a word or topic to search on Wikipedia: ")
    fetch_wikipedia_summary(word)
