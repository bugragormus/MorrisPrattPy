def morris_pratt_search(patterns, text):
    text = text.lower() # Algoritma büyük/küçük harfe duyarlı olduğu için txt dosyasındaki tüm harfleri küçük harfe çeviriyoruz.
    patterns = [p.lower() for p in patterns] # txt dosyasındaki tüm harfleri küçük harf yaptığımız için aradığımız kelimeleri de küçük harf olarak alıyoruz.
    results = {pattern: [] for pattern in patterns} # Sonuçları depolamak için boş bir sözlük oluşturuyoruz.
    m = max([len(pattern) for pattern in patterns]) # Patterns içindeki en uzun öğenin uzunluğunu belirliyoruz.
    n = len(text) # txt dosyasının uzunluğunu belirliyoruz.
    
    # Önbellek tablolarını oluşturma işlemi
    tables = {}
    for pattern in patterns:
        table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = table[j-1]
            if pattern[j] == pattern[i]:
                j += 1
            table[i] = j
        tables[pattern] = table

    # Metin dizesinde arama işlemi
    for i in range(n - m + 1):
        for pattern in patterns:
            j = 0
            for k in range(len(pattern)):
                if pattern[j] == text[i+k]:
                    j += 1
                    if j == len(pattern):
                        results[pattern].append(i)
                        j = tables[pattern][j-1]
                else:
                    j = tables[pattern][j-1]
    
    # Sonuçları ekrana yazdırma işlemi
    for pattern in patterns:
        print("\nAranan öğe:", pattern, "- Toplam tekrar sayısı:", len(results[pattern]))


# Örnek kullanım
with open("alice_in_wonderland.txt", "r") as f: # İçerisinde arama yapılacak olan txt dosyasının dosya yolunu yazıyoruz.
    text = f.read()
    patterns = ["upon", "sigh", "Dormouse", "jury-box", "swim"] # Aranacak ögeleri liste elemanı olarak yazıyoruz. Küçük/büyük harf önemli değil.
    morris_pratt_search(patterns, text) # Arama ve yazdırma işlemini yapacak olan fonksiyonumuzu çağırıyoruz.