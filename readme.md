# Selenium Selectors by XPATH

- Absolute : ***/*** ile başlar

- Relative : ***//*** ile başlar

- starts-with() : ***"//tagname[starts-with(@Attribute="Value")]"***
Elementlerden belirtilen attribute için, belirtilen value ile başlayanları seçer.

- contains() : ***"//tagname[contains(@Attribute="Value")]"***
Elementlerden belirtilen attribute için, içinde belirtilen value geçenleriseçer.

- text(): ***"//tagname[text()="Value"]"***
Elementin text'ini tam uyacak şekilde kontrol eder ve uyuyorsa seçer.

- Bir a elemntinin text'ine göre bulmak:  ***"//tagname[normalize-space()='text']"***
Örnek :  "//a[normalize-space()='Kullanıcı telefonu / e-posta / kullanıcı adı']"
Burada elemnitin text'ini büyük-küçük harf uymasada seçer.

- Bir elementi attribute ile bulmak : ***"//tagname[@Attribute="Value"]"***
Örnek: "//a[@href='/signup/phone-or-email/email']"

- AND- OR : ***"//tagname[@Attribute="Value" and Attribute="Value"]"***
Birden fazla koşul eşlemesi için kullanılır.

- Parent- Child -Self : ***"//tagname[@Attribute="Value"]//parent-child-self::tagname"***
  - parent  : seçili elementin ana elementini seçer.
  - child   : seçili elementin tüm alt-elementlerini seçer
  - self    : seçili elementi seçer
