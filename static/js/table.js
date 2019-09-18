$(document).ready(function($){
    function creat_html_table(tbl_data){
        var tbl='<tbody>';
            $.each(tbl_data,function(index, val){
                var row_id = val['row_id'];
                    tbl +='<tr row_id="'+row_id+'">';
                        tbl += '<td>'+'hhhhhhhh'+val["fname"]+'</td>';
                        tbl += '<td>'+val["lname"]+'</td>';
                        tbl += '<td>'+val["phone"]+'</td>';
                        tbl += '<td>'+val["email"]+'</td>';
                        tbl += '<td>'+val["address"]+'</td>';
                    tbl +='</tr>';
                
            })
        tbl+='<tbody>';
       
    }
    creat_html_table(1,{
        fname: 'mine',
        lname: 'mimuyt',
        phone: '009099',
        email: 'opoi@jjj.mmo',
        address: 'ss501'
    }); $(document).find('.tbl_user_data').html(tbl);
});


$(document).ready(function() {
    $('#system-search').keyup( function() {
       var that = this;
        var tableBody = $('.table-list-search tbody');
        var tableRowsClass = $('.table-list-search tbody tr');
        $('.search-sf').remove();
        tableRowsClass.each( function(i, val) {
            var rowText = $(val).text().toLowerCase();
            var inputText = $(that).val().toLowerCase();
            if(inputText != '')
            {
                $('.search-query-sf').remove();
                tableBody.prepend('<tr class="search-query-sf"><td colspan="6"><strong>Searching for: "'
                    + $(that).val()
                    + '"</strong></td></tr>');
            }
            else
            {
                $('.search-query-sf').remove();
            }

            if( rowText.indexOf( inputText ) == -1 )
            {
                //hide rows
                tableRowsClass.eq(i).hide(); 
            }
            else
            {
                $('.search-sf').remove();
                tableRowsClass.eq(i).show();
            }
        });
        //all tr elements are hidden
        if(tableRowsClass.children(':visible').length == 0)
        {
            tableBody.append('<tr class="search-sf"><td class="text-muted" colspan="6">No entries found.</td></tr>');
        }
    });
});
