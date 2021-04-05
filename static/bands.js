// Data
let bands = [];
let info = [];

// NavBar
async function renderHome() {
    await $.ajax({
        type: "POST",
        url: "/",
        data: JSON.stringify({}),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(result) {
            console.log(result);
            bands = result["bands"]
            info = result["info"]
            console.log(bands)
            console.log(info)
        },
        error: function(request, status, error) {
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
    for(let i = info.length - 1; i >= 0; i--) {
        let button = "<div class='card col-5'><a href='/view/"+ info[i]["id"] + "'><h1 class='row justify-content-center'>" + info[i]["band"] + "</h1><div class='row justify-content-center'><img class='imgcard' src='" + info[i]["image"] + "' alt='" + info[i]["band"] + "'></img></div></a></div>";
        $("#results").append(button);
    }
}
$("#searchResults").hide();
$("#searchButton").click(() => {
    let query = $("#search").val();
    $("#content").hide();
    $("#searchResults").empty();
    $("#searchResults").show();
    $.ajax({
        type: "POST",
        url: "/search",
        data: JSON.stringify({
            query
        }),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(result) {
            console.log(result);
            if(result["bands"].length == 0) {
                $("#searchResults").append("<h2>No Results</h2>");
                return;
            }
            for(let i = 0; i < result["bands"].length; i++) {
                let button = "<div class='card col-5'><a href='/view/"+ result["bands"][i]["id"] + "'><h1 class='row justify-content-center'>" + result["bands"][i]["band"] + "</h1><div class='row justify-content-center'><img class='imgcard' src='" + result["bands"][i]["image"] + "' alt='" + result["bands"][i]["band"] + "'></img></div></a></div>";
                $("#searchResults").append(button);
            }
        },
        error: function(request, status, error) {
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
    $("#search").val("");
});

// Create entry
$("#createButton").click(function() {
    $("results").empty();
    let band = $("#band").val();
    let description = $("#description").val();
    let image = $("#image").val();
    let yearFormed = $("#yearFormed").val();
    let albums = [$("#album1").val(), $("#album2").val(), $("#album3").val()].filter(val => { return val != "" });
    if(band.trim() == "") {
        $("#message").html("Please enter a band").css("color", "red");
        $("#band").focus();
        return;
    } else if(description.trim() == "") {
        $("#message").html("Please enter a description").css("color", "red");
        $("#description").focus();
        return;
    } else if(image.trim() == "") {
        $("#message").html("Please enter an image").css("color", "red");
        $("#image").focus();
        return;
    } else if(yearFormed.trim() == "") {
        $("#message").html("Please enter a year").css("color", "red");
        $("#yearFormed").focus();
        return;
    } else if(!Number.isInteger(parseInt(yearFormed))) {
        $("#message").html("Please enter a valid year").css("color", "red");
        $("#yearFormed").focus();
        return;
    } else if(albums.length != 3) {
        $("#message").html("Please enter 3 albums").css("color", "red");
        if(albums.length == 0) {
            $("#album1").focus();
        } else if(albums.length == 1) {
            $("#album2").focus();
        } else if(albums.length == 2) {
            $("#album3").focus();
        }
        return;
    }
    $.ajax({
        type: "POST",
        url: "/create/submit",
        data: JSON.stringify({
            band,
            image,
            description,
            yearFormed,
            albums
        }),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(result) {
            console.log(result);
            bands = result["bands"]
            info = result["info"]
            console.log(bands)
            console.log(info)
            $("#message").html("New item successfully created!").css("color", "green");
            let button = "<div class='card col-5'><a href='/view/"+ result["new"]["id"] + "'><h1 class='row justify-content-center'>" + result["new"]["band"] + "</h1><div class='row justify-content-center'><img class='imgcard' src='" + result["new"]["image"] + "' alt='" + result["new"]["band"] + "'></img></div></a></div>";
            $("#results").append(button);
        },
        error: function(request, status, error) {
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
            $("#message").html("Error").css("color", "red");
        }
    });
    $("#band").val("");
    $("#band").focus();
    $("#image").val("");
    $("#description").val("");
    $("#yearFormed").val("");
    $("#album1").val("");
    $("#album2").val("");
    $("#album3").val("");
});

// Update entry
$("#bid").hide();
$("#edit").hide();
$("#editButton").click(() => {
    $("#update").val($('#descriptionValue').text());
    $("#description").hide();
    $("#edit").show();
});
$("#discardButton").click(() => {
    $("#update").val("");
    $("#edit").hide();
    $("#description").show();
});
$("#updateButton").click(() => {
    let bid = $("#bid").text();
    let update = $("#update").val();
    if(update == "") {
        $("#message").html("Please enter a new description").css("color", "red");
        return;
    }
    $.ajax({
        type: "POST",
        url: "/update",
        data: JSON.stringify({
            bid,
            update
        }),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(result) {
            console.log(result);
            $("#message").html("Success!").css("color", "green");
            info = result["info"]
            window.location.replace("/view/" + bid);
        },
        error: function(request, status, error) {
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
            $("#message").html("Error").css("color", "red");
        }
    });
    $("#edit").hide();
    $("#description").show();
});

// Delete entry
$("#p0").hide();
$("#p1").hide();
$("#p2").hide();
$("#0undo").hide();
$("#1undo").hide();
$("#2undo").hide();
if($("#p0").html() == "True") {
    $("#0").hide();
    $("#0undo").show();
}
if($("#p1").html() == "True") {
    $("#1").hide();
    $("#1undo").show();
}
if($("#p2").html() == "True") {
    $("#2").hide();
    $("#2undo").show();
}
$(".deleteButton").click(function() {
    let bid = $("#bid").text();
    let index = $(this).parent().attr("id");
    console.log(index);
    $.ajax({
        type: "POST",
        url: "/delete",
        data: JSON.stringify({
            bid,
            index
        }),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(result) {
            console.log(result);
            info = result["info"];
            window.location.replace("/view/" + bid);
        },
        error: function(request, status, error) {
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
});
$(".undoButton").click(function() {
    let bid = $("#bid").text();
    let index = $(this).parent().attr("id").substring(0, 1);
    $.ajax({
        type: "POST",
        url: "/undo",
        data: JSON.stringify({
            bid,
            index
        }),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function(result) {
            console.log(result);
            info = result["info"];
            window.location.replace("/view/" + bid);
        },
        error: function(request, status, error) {
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
});