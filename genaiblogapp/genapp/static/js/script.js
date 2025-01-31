var quill = new Quill('#editor-container', {
    theme: 'snow', // You can change this to 'bubble' for a different look
    placeholder: 'Start typing...',
    modules: {
      toolbar: [
        [{ 'header': '1'}, { 'header': '2'}, { 'font': [] }],
        [{ 'list': 'ordered'}, { 'list': 'bullet' }],
        ['bold', 'italic', 'underline'],
        [{ 'align': [] }],
        ['link']
      ]
    }
  });

