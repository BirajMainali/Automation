function openInChrome(url) {
    chrome.runtime.sendMessage({ action: "https:/youtube.com", url: url });
};
openInChrome(url)

// background
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
    if (message.action == "https:/youtube.com") window.open(message.url);
});