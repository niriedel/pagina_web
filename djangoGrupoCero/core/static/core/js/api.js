$(document).ready(function () {
    

$("#enviar").click(function(e) {
    e.preventDefault();
    let userSelection = $("#select").val();

    $.get(`https://collectionapi.metmuseum.org/public/collection/v1/search?medium=Paintings&q=${userSelection}`,
    function(firstData){
      let id = 0;
      let newId = 0;
      $('#api-box').append(`
      <div id="painting-cards"></div>
      `);
      $.each(firstData.objectIDs, function(i, item) {
        $.get(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${item}`,
        function(secondData){
          let img = secondData.primaryImageSmall;
          let title = secondData.title;
          let artist = secondData.artistDisplayName;
          let fechaCreacion = secondData.objectDate;
          let department = secondData.department;
          let tipo = secondData.objectName;

          if (!(img === "")) {
            if (id == 0 || id % 3 == 0) {
              newId = id;
              $("#painting-cards").append(`<div class="card-group mb-3 border" id="imagenes${newId}">
                                    </div>`);
            }

            $(`#imagenes${newId}`).append(`<div class="card">
                                      <a target="_blank" href="https://www.metmuseum.org/art/collection/search/${item}"><img class="card-img-top" src="${img}" alt="Card image cap"></a>
                                      <div class="card-body">
                                        <h5 class="card-title">${title}</h5>
                                        <p class="card-text">Creada por el/la artista ${artist} en el año ${fechaCreacion}.</p>
                                      </div>
                                      <div class="card-footer">
                                        <small class="text-muted">Categoria: ${tipo}, ${department}</small>
                                      </div>
                                    </div>`);
            id+=1;
          }
        });
      })
    })

  })

  $('#reiniciar').click(function (e) { 
    e.preventDefault();
    $('#painting-cards').remove();
  });

});
