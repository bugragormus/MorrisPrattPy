# **Morris-Pratt Search Algorithm with Python**

### **Morris-Pratt Algoritması Nedir?**

Morris-Pratt algoritması, bir metin içinde belirli bir kalıbın eşleşip eşleşmediğini bulmak için kullanılan bir dize arama algoritmasıdır. Özellikle uzun metinlerdeki aramaları hızlandırmak için tasarlanmıştır.

Bu algoritma, Brute Force algoritmasına benzer, ancak bazı optimizasyonlar içerir. Brute Force algoritması, kalıp dizesini tek tek metindeki tüm konumlara karşı kontrol ederek çalışırken, Morris-Pratt algoritması, bir önbellek tablosu kullanarak işlem yapar ve daha az karşılaştırma yaparak daha hızlı sonuçlar elde eder.

Algoritmanın çalışma prensibi şu şekildedir: Öncelikle kalıp dizesindeki tüm alt dizelerin ön ekleri için bir önbellek tablosu oluşturulur. Ardından, metin dizesindeki karakterleri tek tek kontrol ederek kalıp dizesindeki karakterlerle karşılaştırılır. Eğer bir karakter eşleşmiyorsa, önbellek tablosuna bakılır ve kalıp dizesindeki bir önceki karakterle eşleşen karakterin indeksine kadar atlanır. Eğer bir karakter eşleşirse, bir sonraki karaktere geçilir ve eşleşen karakterlerin sayısı ölçülür. Eşleşen karakter sayısı, kalıp dizesinin uzunluğuna eşit olduğunda, bir eşleşme olduğu anlaşılır. Bu şekilde, Morris-Pratt algoritması Brute Force algoritmasına göre daha az karşılaştırma yaparak daha hızlı bir şekilde sonuç elde eder. Bu algoritma, özellikle büyük metinlerde ve karmaşık kalıp dizelerinde kullanıldığında etkili bir şekilde çalışır.


### **Morris-Pratt Algoritması Çalışma Analizi**

Morris-Pratt algoritmasının çalışma zamanı O(m+n)'dir, burada m kalıp dizesinin uzunluğunu, n ise metin dizesinin uzunluğunu temsil eder. Bu, algoritmanın Brute Force algoritmasına kıyasla daha hızlı olduğu anlamına gelir.

- En iyi çalışma zamanı sınırları, kalıp dizesi ve metin dizesi arasında herhangi bir eşleşme olmadığında gerçekleşir ve O(m)'dir. Bu durumda, önbellek tablosu yalnızca bir kez oluşturulur ve metin dizesindeki tüm karakterler sadece bir kez kontrol edilir.

- En kötü çalışma zamanı sınırları, önbellek tablosu oluşturma ve metin dizesi karakterlerini kontrol etme sürecinde en kötü senaryoda gerçekleşir. Bu senaryo, kalıp dizesinin metin dizesinin her karakteriyle eşleşmediği durumlarda ortaya çıkar. Bu durumda, önbellek tablosu O(m) zamanında oluşturulur ve metin dizesindeki her bir karakter O(n) kez kontrol edilir. Bu durumda, çalışma zamanı O(mn) olur.

- Ortalama çalışma zamanı sınırları, algoritmanın verilen bir girdi boyutu için beklenen çalışma zamanıdır. Morris-Pratt algoritması için ortalama çalışma zamanı, algoritmanın tüm olası kalıp dizesi ve metin dizesi çiftleri için çalışma zamanlarının ortalamasını alarak bulunur. Bu analiz oldukça karmaşıktır ve genellikle pratik uygulamalarda kullanılmaz.

Kısacası, Morris-Pratt algoritmasının çalışma zamanı analizi, önbellek tablosu oluşturma ve metin dizesindeki karakterleri kontrol etme süreçleriyle ilgilidir. Önbellek tablosu oluşturma işlemi, kalıp dizesinin uzunluğuna bağlı olarak O(m) zamanında gerçekleşir. Metin dizesindeki karakterleri kontrol etme işlemi, en kötü durumda, her karakter için önbellek tablosuna bakarak O(m) zamanında gerçekleşir. Bu nedenle, Morris-Pratt algoritmasının en kötü çalışma zamanı O(mn) olarak hesaplanır. Ancak, algoritmanın önbellek tablosu kullanarak işlem yapması, en iyi durumda sadece O(m) zamanında çalışmasını sağlar.
