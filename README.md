#
<h1 align="center">
  <strong>plotX</strong>
</h1>

<div>
  <p align="center">
    <img
      src="https://github.com/We2Am-BaSsem/plotX/blob/main/logo.jpg"
      alt="logo"
    />
  </p>
</div>

# Description
<p>
  GUI program that plots your input f(x) in a specific interval [minX,maxX] and
  display the figure.
</p>
<p>You can save plots as images in your local machine.</p>
<p>
  plotX has a beautiful interactive error message to inform the user if he
  messes up.
</p>

# Test Report 
> [Report](https://rawcdn.githack.com/We2Am-BaSsem/plotX/5f261f40a6264cc990757306473bba904ab1686a/Report/index.html)
# Dependencies
<ol>
  <li>
    <img
      style="width: 35px; height: 35px"
      src="https://user-images.githubusercontent.com/58189568/147625496-fe96da92-ff8b-4994-949b-0802a0fc2b86.png"
      alt="logo"
    />
    Python
  </li>
  <li>
    <img
      style="width: 35px; height: 35px"
      src="https://user-images.githubusercontent.com/58189568/147625829-bb66dac6-3cd0-48cc-923b-b6522c169a60.png"
      alt="logo"
    />
    PyQt5
  </li>
  <li>    
    <img
      style="width: 35px; height: 35px"
      src="https://user-images.githubusercontent.com/58189568/147625981-8ee36404-9d4c-4bc2-8e30-2a8c0ed909ff.png"
      alt="logo"
    />
    Pytest
  </li>
  <li>    
    <img
      style="width: 35px; height: 35px"
      src="https://user-images.githubusercontent.com/58189568/147626016-f6d25de4-e275-4bb0-aea9-d99933303f46.png"
      alt="logo"
    />
   Allure-Reporter
  </li>
</ol>

<p>
  To run the Program You need Python and PyQt5 to open the application with
  command:
</p>

```bash python3 app.py ```

<p>
  While test scripts written with Pytest and Allure-Report for python to
  generate the report:
</p>

```bash ./RunTest.sh ``` # Screenshots
<div>
  <p align="center">
    Application GUI
    <img
      src="https://github.com/We2Am-BaSsem/plotX/blob/main/screenshots/Screenshot%20from%202021-12-29%2005-30-32.png"
      alt="logo"
    />
  </p>
</div>

<div>
  <p align="center">
    If user enter empty data
    <img
      src="https://github.com/We2Am-BaSsem/plotX/blob/main/screenshots/Screenshot%20from%202021-12-29%2005-31-08.png"
      alt="logo"
    />
  </p>
</div>

<div>
  If user enter min x greater than max x the application will swap their values,
  plot the function and inform the user
  <p align="center">
    <img
      src="https://github.com/We2Am-BaSsem/plotX/blob/main/screenshots/Screenshot%20from%202021-12-29%2005-32-15.png"
      alt="logo"
    />
  </p>
  <p align="center">
    <img
      src="https://github.com/We2Am-BaSsem/plotX/blob/main/screenshots/Screenshot%20from%202021-12-29%2005-31-24.png"
      alt="logo"
    />
  </p>
</div>

<div>
  <p align="center">
    <img
      src="https://github.com/We2Am-BaSsem/plotX/blob/main/screenshots/Screenshot%20from%202021-12-29%2005-32-35.png"
      alt="logo"
    />
  </p>
</div>
