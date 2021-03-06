export default {
  init: function() {
    var quitConfirm = false;
    function checkUploads(ev) {
      if (quitConfirm) { return; }

      var filesAddedCount = $('#id_submissions').data('files-added');
      var filesUploadingCount = $('#id_submissions').data('files-uploading');
      if (!filesAddedCount && !filesUploadingCount) {
        quitConfirm = true;
        return;
      }

      if(filesAddedCount) {
        var r = confirm(gettext("Certains de vos fichiers n'ont pas étés téléversés. Êtes-vous sûr ?"));
        if (r == true) { quitConfirm = true; }
      }

      if(filesUploadingCount) {
        var r = confirm(gettext("Certains de vos fichiers ne sont pas complètement téléversés. Êtes-vous sûr ?"));
        if (r == true) { quitConfirm = true; }
      }

      if (quitConfirm) { return; }

      ev.preventDefault();
    }

    $('form').submit(checkUploads);
    $('a:not(form a)').click(checkUploads);
    window.onbeforeunload = checkUploads;
  },
};
