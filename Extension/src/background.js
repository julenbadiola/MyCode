var done = false;

chrome.tabs.onUpdated.addListener(function( tabId,  changeInfo,  tab) {
    // if(tab.url.includes("indexInternal.es?action=")){
    //    	alert("Searching for bonuses... If it takes too long, please sign in again.");
    // }
    if(tab.url.includes("=internalEvoucher") && !done){
       	alert("Bonus found! CODE: BSOGENERAL19");
       	done = true;
    }
})