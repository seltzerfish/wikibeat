% rebase("layout.tpl", title="Store Report")

<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 15%">
      <h4 style="text-align: center">Items Sold</h4>
    </div>
  <div class="row">
    <div class="twelve column" style="text-align: center">
      <a class="button button-primary" style="text-align: left" href="/">Return to Home</a>
    </div>
  </div>
  </div>
    <div class="row">
    </div>
  <div class="row" style="text-align: center; margin-top: 5%">
    <table class="u-full-width">
      <thead>
        <tr>
          <th>Name</th>
          <th>Amount Sold</th>
          <th>Revenue</th>
        </tr>
      </thead>
      <tbody style='font-weight: 300'>
        %for i in range(0, len(table)):
        <tr>
          %for j in table[i].keys():
            % if j == 'revenue':
              % revenue_str = '${:,.2f}'.format(table[i][j])
              <td>{{ revenue_str }}</td>
            % else:
              <td>{{ table[i][j] }}</td>
            %end
          %end
        </tr>
        %end
      </tbody>
    </table>
  </div>

  <hr>

  <div class="row" style="text-align: left; margin-top: 5%">
    <b>Total Revenue:</b> {{ total }}
  </div>
</div>