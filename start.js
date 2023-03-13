const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

async function example() {
  // Указываем опции для запуска Chrome
  const options = new chrome.Options();
  options.addArguments('--disable-extensions');
  options.addArguments('--headless');

  // Создаем новый экземпляр веб-драйвера
  const driver = await new Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .build();

  try {
    // Переходим на страницу
    await driver.get('https://www.example.com');

    // Находим элемент по селектору и нажимаем на него
    const element = await driver.findElement(By.css('#myButton'));
    await element.click();

    // Ждем, пока страница загрузится
    await driver.wait(until.titleIs('New Page Title'), 1000);
  } finally {
    // Закрываем веб-драйвер
    await driver.quit();
  }
}

example();