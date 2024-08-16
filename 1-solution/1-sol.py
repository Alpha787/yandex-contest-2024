import textwrap
import re



def text_formatting(input: str):
  
  # Если на вводе пустая строка,
  # вывести None
  if not input:
    return None
  
  maxWordLen = max(input.replace(",", " ").split(), key=len)
  # Вычислить макс длину предложения
  maxStrLen = len(maxWordLen)*3
  print(maxStrLen)
  # оборачиваем текст по ширине maxStrLen
  wrapper = textwrap.TextWrapper(width=maxStrLen)
  word_list = wrapper.wrap(text=input)
    
  for index, element in enumerate(word_list):
    # Если найден конец слова, пробел, запятую,
    # склеить конец слова и запятую
    if re.search(r'[a-z] ,', element):
      word_list[index] = re.sub(r' ,', r',', element)
    # Если найден конец слова, запятая и начало другого слова,
    # поставить пробел после запятой
    elif re.search(r'[a-z],[a-z]', element):
      word_list[index] = re.sub(r',([a-z])', r', \1', element)
    
    updated_text = wrapper.fill(' '.join(word_list))
  print(updated_text)

# Функция выполняет свою задачу, только выдача отличается от условия
# В условии указано: 
# 'если слово не входит на строку i, строка i заканчивается, а слово будет записано на строке (i+1)'

# Однако моя функция переносит это слово

if __name__ == '__main__':
  input1 = "once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched"
  input2 = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex"
  input3 = ""
  
  print(text_formatting(input1))
  print("===============================")
  print(text_formatting(input2))
  print("===============================")
  print(text_formatting(input3))
  print("===============================")
    