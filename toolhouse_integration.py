from toolhouse import Toolhouse

def use_toolhouse(query):
    toolhouse = Toolhouse()
    results = toolhouse.semantic_search(query)
    return results

if __name__ == "__main__":
    query = "Nearest washroom in Italy"
    print("Toolhouse Results:", use_toolhouse(query))
