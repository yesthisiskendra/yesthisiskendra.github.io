// var folderpath = Folder.desktop + '/imdb_graphs'
// var folderpath = Folder.desktop + '/imdb_graphs/Universal_TN__2018.pdf'
var folderpath = Folder.desktop + '/imdb_graphs/Walt_Disney_TN__2018.pdf'
// alert(aiFilePath)

function changeFont(docRef){
	alert('getting here!', docRef)
	if (app.documents.length > 0 ) {
		for (i = 0; i < app.activeDocument.textFrames.length; i++) {
			textArtRange = app.activeDocument.textFrames[i].textRange;
			// alert(app.textFonts.getByName('Georgia'))
			textArtRange.characterAttributes.textFont = app.textFonts.getByName('Georgia');
		}
	}
}


docRef = open(File(folderpath));
changeFont(docRef)

// for (i = 0; i < docRef.length; i++) {
//     var file = docRef[i];
//     changeFont(file)
//     // do things with file
// }



