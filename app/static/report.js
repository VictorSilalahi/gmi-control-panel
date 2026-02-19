const { jsPDF } = window.jspdf;

export async function createPDF(elementId, judul_report, nama_file) {

  const header_string = judul_report;
  $("#headerReport").html(header_string);

  const element = document.getElementById(elementId);
  
  // 1. Capture the HTML as a canvas
  const canvas = await html2canvas(element, {
    scale: 2, // Improves resolution for high-quality printing
    useCORS: true, // Allows cross-origin images
    logging: false
  });

  // 2. Convert canvas to image data
  const imgData = canvas.toDataURL('image/png');

  // 3. Initialize jsPDF (A4 size, portrait)
  const imgWidth = 210; // A4 width in mm
  const pageHeight = 295;
  const imgHeight = (canvas.height * imgWidth) / canvas.width;
  var heightLeft = imgHeight;

  const pdf = new jsPDF('p', 'mm', 'a4');

  var position = 0;

  pdf.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);
  heightLeft -= pageHeight;

  while (heightLeft >= 0) {
        position = heightLeft - imgHeight;
        pdf.addPage();
        pdf.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);
        heightLeft = heightLeft - pageHeight;
  }
  pdf.save( nama_file+'.pdf');
};

