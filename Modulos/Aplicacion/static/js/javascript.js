let dataTable;
let dataTableInitialized = false;

const dataTableOptions = {
    pageLength: 4,
    destroy: true,
    language: {
        url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        lengthMenu: "Mostrar _MENU_ registros",
        info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
    }
};

const initDataTable = async () => {
    if (dataTableInitialized) {
        dataTable.destroy();
    }

    dataTable = $(".table").DataTable(dataTableOptions);

    dataTableInitialized = true;
}

window.addEventListener("load", async () => {
    await initDataTable()
})

document.querySelector('.profile-container').addEventListener('click', function () {
    var profileOption = document.querySelector('.profile-option');
    if (profileOption.classList.contains('expand')) {
        profileOption.classList.remove('expand');
        profileOption.style.display = 'none';
    } else {
        profileOption.classList.add('expand');
        profileOption.style.display = 'flex';
    }
});

document.getElementById("txtTipoUsuario").onchange = function () {
    if (this.value === "Externo") {
        document.getElementById("interno").selected = true;
        document.getElementById("txtTipoPrestamo").disabled = true;
    }

    else {
        document.getElementById("interno").selected = false;
        document.getElementById("txtTipoPrestamo").disabled = false;
    }
};

