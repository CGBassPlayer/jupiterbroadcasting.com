const wufooFormUrl = new URL("https://jblive.wufoo.com/forms/w7x2r7/")
const form = document.querySelector("#contact-form")

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

// reference: https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_forms_through_JavaScript
async function sendData() {
  fetchIdStamp().then((data)=> {
    idstamp = data;
  })

  const formData = new FormData(form);
  formData.append("idstamp", idstamp)

  const response = await fetch("UPDATE ME", {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    window.location.href =`${wufooFormUrl}`;
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  sendData();
})
