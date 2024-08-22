# решение задачи
def lexicographical_compare(n, q, words, queries):
  # Использовать функцию map() для разбива ввода на данные
  
  # Сортируем словарь и созраняем оригинальные индексы
  sorted_words_with_indicies = sorted((word, index) for index, word in enumerate(words))
  
  results = []
  for k, p in queries:
    matching_words = [(word, index) for word, index in sorted_words_with_indicies if word.startswith(p)]
    
    # Проверяем, достаточно ли слов для k
    if k <= len(matching_words):
      results.append(matching_words[k-1][1] + 1) # вернуть индекс слова
    else:
      results.append(-1) # убрать, если нет такого слова
  
  return results
# Формат ввода:
# Первая строка: первое число - размер словаря, второе - количество запросов
# Словарь слов, в которые идут запросы
# Запросы: идут после словаря

input1 = """
      10 3
      aa
      aaa
      aab
      ab
      abc
      ac
      ba
      daa
      dab
      dadba
      4 a 
      2 da
      4 da
"""
output1 = """
          4
          9
          -1
          """

if __name__ == '__main__':
  
  # Ввод данных из терминала
  # n, q = map(int, input().split())
  # words = [input().strip() for _ in range(n)]
  # queries = [tuple(input().strip().split()) for _ in range(q)]
  # queries = [(int(k), p) for k, p in queries]
  
  # Ввод тестовых данных
  n, q = map(int, (10, 3))
  words = ['aa', 'aaa', 'aab', 'ab', 'abc', 'ac', 'ba', 'daa', 'dab', 'dadba']
  queries = [(4, 'a'), (2, 'da'), (4, 'da')]
  queries = [(int(k), p) for k, p in queries]
  
  # Вывод данных
  # print(lexicographical_compare(input1))
  print(lexicographical_compare(n, q, words, queries))
    