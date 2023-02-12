const initialize = () => {

    //retrieving variables from HTML
    const onboardButton = document.getElementById('connectButton');
    const returnAccountAddress = document.getElementById('returnAccountAddress');
    const returnAccountBalance = document.getElementById('returnAccountBalance');
    const onboareturnChainIDrdButton = document.getElementById('returnChainID');


    const isMetaMaskInstalled = () => {
        const { ethereum } = window;
        return Boolean(ethereum && ethereum.isMetaMask);
    };

    const onClickConnect = async() => {

        //MetaMask login
        try {
            // window.alert("click")
            ethereum.request({ method: 'eth_requestAccounts' });

            window.onload = function MetaMaskClientCheck() {
                returnAccountAddress.innerHTML = "Signed In As: " + ethereum.selectedAddress;
                //console.log("returnAccountAddress.innerHTML is", returnAccountAddress.innerHTML)
            };

            window.alert("Connected to MetaMask!")

            returnAccountAddress.value = ethereum.selectedAddress;

        } catch (error) {
            window.alert("Error is from connectMetaMask.js" + error)
        };

    };

    const MetaMaskClientCheck = () => {
        //checks whether MetaMask is installed by calling isMetaMaskInstalled() and calls onClickConnect if its installed
        if (!isMetaMaskInstalled()) {
            window.alert('Please Install MetaMask');
        } else {
            onboardButton.innerText = 'Connect to MetaMask';
            onboardButton.onclick = onClickConnect;
        };
    };

    //MetaMaskClientCheck() function is the first thing called in connectMetaMask.js
    MetaMaskClientCheck()

};
window.addEventListener('DOMContentLoaded', initialize);