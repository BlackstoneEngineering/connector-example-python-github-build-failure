# What 
This is a simple python webapp that turns a IoT light on / off using mbed Device Connector depending on the status of a github repo build status. 

# Why
Because I want to build something simple, but useful demonstrating IoT using [ARM mbed Device Connector](http://connector.mbed.com)

# Pre-Requirements
* The [mbed_connector_api](https://github.com/ARMmbed/mbed-connector-api-python) python package
* Python 2.7.9+
* device running [mbed-client-example](https://github.com/ARMmbed/mbed-client-examples)
    * Requires [developer.mbed.org](http://developer.mbed.org) / [connector.mbed.com](http://connector.mbed.com) account

# How
1. Load board with [mbed-client-example](https://github.com/ARMmbed/mbed-client-examples). Plug in power and ethernet to connect the board to the internet.
   * **Optional Bonus :** use relay to control super awesome police siren instead of onboard LED on board. To do this replace the deffinition of `led1` in `source/main.cpp`.
   ```cpp
   DigitalOut led1(D3); // where D3 controls the relay
   ```
2. Modify the values in the `standalone.py` script. You will need to fill in the [token](https://connector.mbed.com/#accesskeys) field, the `endpoint` field, and you can change repo the build badge is on by changing the `owner`, `repo`, and `ref` fields. 
3. Run the standalone python script on an internet connected computer. 
```python
python ./src/standalone.py
```

# Liscense
Apache 2.0, see the Liscense file. It means you are free to re-use it in personal or commercial but make sure to give credit where its due. Preferred credit in the form of backlinks to this repo. 
