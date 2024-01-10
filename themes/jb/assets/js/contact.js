const wufooFormUrl = new URL("https://jblive.wufoo.com/forms/w7x2r7/")

async function fetchIdStamp() {
    try {
      const response = await fetch(wufooFormUrl);
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      const data = new DOMParser().parseFromString(await response.text(), "text/html");
      idstamp = data.getElementById("idstamp");
      return idstamp.value;

    } catch (error) {
      console.error('Fetch error:', error);
    }
  }
  
  fetchIdStamp().then((data) => {
    // This is where you can use 'data' outside the function, after the fetch has completed
    console.log(data);
  });
