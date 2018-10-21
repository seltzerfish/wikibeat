% rebase("layout.tpl", title="Store App - Orders")

<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 15%">
      <h4 style="text-align: center">Orders</h4>
    </div>
  <div class="row">
    <div class="one-half column">
      <a class="button button-primary" style="text-align: right" href="/add/order/{{new_id}}">New Checkout</a>
    </div>
    <div class="one-half column">
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
          <th>ID</th>
          <th>Total</th>
          <th>Date</th>
          <th></th>
        </tr>
      </thead>
      <tbody style='font-weight: 300'>
        %for i in range(0, len(table)):
        <tr>
          %for j in table[i].keys():
            % if j == 'total':
              % total_str = '${:,.2f}'.format(table[i][j])
              <td>{{ total_str }}</td>
            % else:
              <td>{{ table[i][j] }}</td>
            %end
          %end
          <td><a class="button button-primary" href="order/{{table[i]['id']}}" style="background-color: #e54b4b; border-color: #e54b4b; ">Details</a></td>
        </tr>
        %end
      </tbody>
    </table>
  </div>
</div>
