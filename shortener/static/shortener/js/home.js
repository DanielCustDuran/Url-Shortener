formShortener = null

$(document).ready(function () {
    formShortener = new FormShortener() 
})

function FormShortener() {
    this.$collection_steps = $("#collection_steps")
	this.init()
}
FormShortener.prototype.init = function () {
    console.log("__init__")
	// this.$tipo.select2()
    // this.$udm.on("change", this, this.change_Udm)
}