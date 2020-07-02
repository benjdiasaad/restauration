$(document).ready(function() {
    $(".menu a.item.link").on('click', function(event){
        event.preventDefault();
        let id = event.target.getAttribute('href')
        $('html, body').animate({
            scrollTop: $(id).offset().top
        }, 1000, function(){
            window.location.hash = id;
        })
    })
})

$(document).ready(function() {
    $('.ui.menu .ui.dropdown').dropdown({on: 'click'});
    $('.ui.menu a.item').on('click', function() { $(this).addClass('active').siblings().removeClass('active'); });
});

$(document).ready(function() {
    $('.ui.form').form({
        fields: {
          username: {
            identifier  : 'username',
            rules: [
              { type   : 'empty', prompt : 'Please enter your username' }
            ]
          },
          password: {
            identifier  : 'password',
            rules: [
              { type   : 'empty', prompt : 'Please enter your password' },
              { type   : 'length[6]', prompt : 'Your password must be at least 6 characters' }
            ]
          }
        }
      })
    ;
  })
;