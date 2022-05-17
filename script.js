$(document).ready(function () {

  var artistasTipoArte = ["Alberto Fernandez","Juanito Perez","Pablo Pinto","Dadaismo", "Medieval","Impresionismo", ];

  function autocomplete(inp, arr) {

    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
    var currentFocus;
    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
          /*check if the item starts with the same letters as the text field value:*/
          if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            /*create a DIV element for each matching element:*/
            b = document.createElement("DIV");
            /*make the matching letters bold:*/
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            /*insert a input field that will hold the current array item's value:*/
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function(e) {
                /*insert the value for the autocomplete text field:*/
                inp.value = this.getElementsByTagName("input")[0].value;
                /*close the list of autocompleted values,
                (or any other open lists of autocompleted values:*/
                closeAllLists();
            });
            a.appendChild(b);
          }
        }
    });
    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
          /*If the arrow DOWN key is pressed,
          increase the currentFocus variable:*/
          currentFocus++;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 38) { //up
          /*If the arrow UP key is pressed,
          decrease the currentFocus variable:*/
          currentFocus--;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 13) {
          /*If the ENTER key is pressed, prevent the form from being submitted,*/
          e.preventDefault();
          if (currentFocus > -1) {
            /*and simulate a click on the "active" item:*/
            if (x) x[currentFocus].click();
          }
        }
    });
    function addActive(x) {
      /*a function to classify an item as "active":*/
      if (!x) return false;
      /*start by removing the "active" class on all items:*/
      removeActive(x);
      if (currentFocus >= x.length) currentFocus = 0;
      if (currentFocus < 0) currentFocus = (x.length - 1);
      /*add class "autocomplete-active":*/
      x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
      /*a function to remove the "active" class from all autocomplete items:*/
      for (var i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
      }
    }
    function closeAllLists(elmnt) {
      /*close all autocomplete lists in the document,
      except the one passed as an argument:*/
      var x = document.getElementsByClassName("autocomplete-items");
      for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
  } 

  autocomplete(document.getElementById("myInput"), artistasTipoArte);

  // $("#enviar").click(function() {
  //   $.get("https://www.themealdb.com/api/json/v1/1/categories.php",
  //   function(data){
  //     $.each(data.categories, function(i, item) {
  //       $("#categorias").append(`<p>${item.idCategory}<p>
  //                                 <img src="${item.strCategoryThumb}"
  //                                 <p>${item.strCategoryDescription}</p>`);
  //     })
  //   })
  // })

  $("#enviar").click(function() {
    $.get("https://collectionapi.metmuseum.org/public/collection/v1/search?medium=Paintings&q=sunflower",
    function(firstData){
      let id = 0;
      let newId = 0;
      $.each(firstData.objectIDs, function(i, item) {
        $.get(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${item}`,
        function(secondData){
          let img = secondData.primaryImageSmall;
          let title = secondData.title;
          let artist = secondData.artistDisplayName;
          let fechaCreacion = secondData.objectDate;
          let department = secondData.department;
          let tipo = secondData.objectName;

            if (id == 0 || id % 3 == 0) {
              newId = id;
              $("#categorias").append(`<div class="card-group" id="imagenes${newId}">
                                    </div>`);
            }

            $(`#imagenes${newId}`).append(`<div class="card">
                                    <p>Iteration index: ${id}</p>
                                    <img class="card-img-top" src="${img}" alt="Card image cap">
                                      <div class="card-body">
                                        <h5 class="card-title">${title}</h5>
                                        <p class="card-text">Creada por el artista ${artist} en el año ${fechaCreacion}.</p>
                                      </div>
                                      <div class="card-footer">
                                        <small class="text-muted">Categoria: ${tipo}, ${department}</small>
                                      </div>
                                    </div>`);
          id+=1;
        });
      })
    })
  })



  // let paintingIds = [];

  // $("#enviar").click(function() {

  //   $.get("https://collectionapi.metmuseum.org/public/collection/v1/search?medium=Paintings&q=sunflower",
  //   function(firstData){
  //     let id = 0;
  //     let newId = 0;
  //     $.each(firstData.objectIDs, function(i, item) {
  //       paintingIds.push(item);
  //     });
  //   });

  //   paintingIds.forEach(function (element, idx) {
  //     $.get(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${element}`,
  //     function(SecondData){
  //       let PaintingImage = SecondData.primaryImageSmall;
  //       if (!(PaintingImage === "")){

  //         if (id == 0 || id % 3 == 0) {
  //           let newId = id;
  //           $("#categorias").append(`<div class="card-group" id="imagenes${newId}">
  //                                 </div>`);
  //         }

  //         $(`#imagenes${newId}`).append(`<div class="card">
  //                                 <p>Iteration index: ${id}</p>
  //                                 <img class="card-img-top" src="${SecondData.primaryImageSmall}" alt="Card image cap">
  //                                   <div class="card-body">
  //                                     <h5 class="card-title">Card title</h5>
  //                                     <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
  //                                   </div>
  //                                   <div class="card-footer">
  //                                     <small class="text-muted">Last updated 3 mins ago</small>
  //                                   </div>
  //                                 </div>`);
  //       }
  //       id+=1;
  //     })
  //   });


  //   });

  });

