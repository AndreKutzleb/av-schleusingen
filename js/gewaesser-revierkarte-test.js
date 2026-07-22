(function () {
  var mapRoot = document.getElementById("gewaesser-map-test");
  var waterways = window.AV_GEWASSER_OSM;

  if (!mapRoot || typeof L === "undefined" || !waterways) {
    return;
  }

  function nearestPointIndex(points, target) {
    var nearestIndex = 0;
    var nearestDistance = Infinity;

    points.forEach(function (point, index) {
      var latitudeDistance = point[0] - target[0];
      var longitudeDistance = point[1] - target[1];
      var distance = latitudeDistance * latitudeDistance + longitudeDistance * longitudeDistance;

      if (distance < nearestDistance) {
        nearestDistance = distance;
        nearestIndex = index;
      }
    });

    return nearestIndex;
  }

  function exactSegment(points, start, end) {
    var startIndex = nearestPointIndex(points, start);
    var endIndex = nearestPointIndex(points, end);
    var firstIndex = Math.min(startIndex, endIndex);
    var lastIndex = Math.max(startIndex, endIndex);

    return points.slice(firstIndex, lastIndex + 1);
  }

  var features = [
    {
      id: "schleuse",
      group: "flowing",
      styleKey: "schleuse",
      geometryType: "LineString",
      coordinates: waterways.schleuse,
      popupTitle: "Schleuse",
      popupBody: "Exakter OpenStreetMap-Flussverlauf vom Auslauf der Talsperre Ratscher bis in Richtung Zollbr&uuml;ck. Die abschlie&szlig;ende Best&auml;tigung des Grenzpunkts steht noch aus."
    },
    {
      id: "schleuse-jagdgebiet",
      group: "notes",
      styleKey: "warning",
      geometryType: "LineString",
      coordinates: exactSegment(
        waterways.schleuse,
        [50.5002, 10.7350],
        [50.4975, 10.7216]
      ),
      popupTitle: "Hinweisbereich unterhalb Rappelsdorf",
      popupBody: "Dieser Hinweis liegt jetzt direkt auf dem OSM-Flussverlauf. Die genaue Ausdehnung des Jagdgebiets muss weiterhin best&auml;tigt werden."
    },
    {
      id: "nahe-nord",
      group: "flowing",
      styleKey: "nahe",
      geometryType: "LineString",
      coordinates: exactSegment(
        waterways.nahe,
        [50.5344, 10.8168],
        [50.5217, 10.7993]
      ),
      popupTitle: "Nahe Schleusingerneundorf bis Hinternah",
      popupBody: "Exakter OSM-Flussverlauf von der Br&uuml;cke in Schleusingerneundorf bis zur Eisenbahnbr&uuml;cke unterhalb Hinternah."
    },
    {
      id: "nahe-flug",
      group: "flowing",
      styleKey: "fly",
      geometryType: "LineString",
      coordinates: exactSegment(
        waterways.nahe,
        [50.5197, 10.7964],
        [50.5179, 10.7904]
      ),
      popupTitle: "Nahe Flugangelstrecke",
      popupBody: "Exakter OSM-Flussverlauf vom Bereich der M&uuml;hlgraben-Wiedereinm&uuml;ndung bis zum Wehr oberhalb Schleusingen. Die Grenzpunkte werden noch fachlich best&auml;tigt."
    },
    {
      id: "nahe-stadt",
      group: "flowing",
      styleKey: "nahe",
      geometryType: "LineString",
      coordinates: exactSegment(
        waterways.nahe,
        [50.5086, 10.7561],
        [50.5088, 10.7476]
      ),
      popupTitle: "Nahe Schleusingen",
      popupBody: "Exakter OSM-Flussverlauf vom Bereich Schwimmbad Schleusingen bis H&ouml;he Bahnhof / Einm&uuml;ndung Erle."
    },
    {
      id: "erle",
      group: "flowing",
      styleKey: "erle",
      geometryType: "LineString",
      coordinates: waterways.erle,
      popupTitle: "Erle",
      popupBody: "Exakter OpenStreetMap-Flussverlauf von der Vesser-Einm&uuml;ndung bis zur M&uuml;ndung in die Nahe."
    },
    {
      id: "sportplatzteich",
      group: "still",
      styleKey: "still",
      geometryType: "Point",
      coordinates: [50.5121938, 10.7423623],
      popupTitle: "Sportplatzteich",
      popupBody: "Marker auf dem OSM-Wasserfl&auml;chenzentrum am Sportplatzteich."
    },
    {
      id: "langer-teich",
      group: "still",
      styleKey: "still",
      geometryType: "Point",
      coordinates: [50.5120950, 10.7490936],
      popupTitle: "Langer Teich",
      popupBody: "Marker auf dem Mittelpunkt der in OpenStreetMap benannten Wasserfl&auml;che."
    },
    {
      id: "hasselbacher",
      group: "still",
      styleKey: "still",
      geometryType: "Point",
      coordinates: [50.5024164, 10.7412105],
      popupTitle: "Hasselbacher",
      popupBody: "Marker auf der Wasserfl&auml;che unmittelbar an der Hildburgh&auml;user Stra&szlig;e."
    }
  ];

  var styleMap = {
    schleuse: {
      color: "#216869",
      weight: 5,
      opacity: 0.95
    },
    nahe: {
      color: "#1f78b4",
      weight: 5,
      opacity: 0.92
    },
    fly: {
      color: "#d97706",
      weight: 6,
      opacity: 0.95,
      dashArray: "10 8"
    },
    erle: {
      color: "#2d6a4f",
      weight: 5,
      opacity: 0.95
    },
    still: {
      radius: 8,
      fillColor: "#8b5e3c",
      color: "#f5f3ef",
      weight: 2,
      opacity: 1,
      fillOpacity: 0.95
    },
    warning: {
      color: "#9f1239",
      weight: 5,
      opacity: 0.9,
      dashArray: "6 10"
    }
  };

  var map = L.map(mapRoot, {
    scrollWheelZoom: false
  }).setView([50.5125, 10.7705], 13);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>-Mitwirkende'
  }).addTo(map);

  var groupedLayers = {
    flowing: L.featureGroup(),
    still: L.featureGroup(),
    notes: L.featureGroup()
  };

  var activeFilter = "all";

  function bindPopup(layer, feature) {
    layer.bindPopup(
      "<strong>" + feature.popupTitle + "</strong><br>" + feature.popupBody
    );
  }

  features.forEach(function (feature) {
    var layer;

    if (feature.geometryType === "Point") {
      layer = L.circleMarker(feature.coordinates, styleMap[feature.styleKey]);
    } else {
      layer = L.polyline(feature.coordinates, styleMap[feature.styleKey]);
    }

    bindPopup(layer, feature);
    groupedLayers[feature.group].addLayer(layer);
  });

  function currentGroups() {
    if (activeFilter === "all") {
      return ["flowing", "still", "notes"];
    }

    return [activeFilter];
  }

  function refreshMap() {
    Object.keys(groupedLayers).forEach(function (group) {
      map.removeLayer(groupedLayers[group]);
    });

    var boundsLayers = [];

    currentGroups().forEach(function (group) {
      groupedLayers[group].addTo(map);
      boundsLayers.push(groupedLayers[group]);
    });

    if (boundsLayers.length) {
      var collection = L.featureGroup(boundsLayers);
      map.fitBounds(collection.getBounds(), {
        padding: [28, 28]
      });
    }
  }

  var filters = document.querySelectorAll(".map-test-filter");

  filters.forEach(function (button) {
    button.addEventListener("click", function () {
      activeFilter = button.getAttribute("data-filter");

      filters.forEach(function (otherButton) {
        otherButton.classList.toggle("is-active", otherButton === button);
      });

      refreshMap();
    });
  });

  refreshMap();
})();
