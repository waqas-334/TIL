# TIL What is is Blockstore API and how it works

`5th May 2024`

I have been looking for solution to backup my app content without actually letting users login. Like some id or anything that can be retreived even when the app is reinstalled or user updates the devices.

I stumbled upon `Blockstore` API by Google which let's you store a 16 Byte array and can retreive late. It looks simple and promosing.

So far, I have been able to test on an emulator and the results are as follow:

- The payloads survives app uninstall and reinstall
- It does not matter if the user is logged in to Google or not. Which may be very rare in real life but it works nonetheless. 
- It would return same payload if you saved it when user was not logged into Google, and retreived it after logging in

### Side effects:
- As it uses Google play services API, so Google Play must be installed on the device to make it work. 

### Future Plans:
- Need to test it on real device. Like saving the payload in emulator after logging in to a Google account and then use the same Google account on a different device retrieve the id and see if it results the same
- Check compatibility: needs to see the supported Android version.