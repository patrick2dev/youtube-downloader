function youtubeSend() {
    let download = $('#download')
        loader = $('.loader')
        button = $('form >button')
        details = $('#details');
  if ($('#url').val() != "") {
    loader.show();
    button.addClass('disabled');
    download.html(``);
    details.hide();
    $('#thumbnail').attr('src', '');
    $.get('http://127.0.0.1:5000/api/youtube', { url: $('#url').val() }, (result) => {
      $('.loader').hide();
      button.removeClass('disabled');
      details.show()
      $('#title').html(`<span class="text-head">TITLE:</span><span class="text">${result.details.title}</span>`);
      $('#views').html(`<span class="text-head">VIEWS:</span><span class="text">${result.details.views} views</span>`);
      $('#author').html(`<span class="text-head">AUTHOR:</span><span class="text">${result.details.author}</span>`);
      $('#thumbnail').attr('src', result.details.thumbnail);
      $.each(result.sources, (id, src) => {
        download.append('<a style="text-decoration:none;color:#fff;" href="'+src.download+'?title='+result.details.title+'"><button>download '+src.resolution+'</button></a>')
      });
    }, "json");
  } else {
    return false;
  }
}