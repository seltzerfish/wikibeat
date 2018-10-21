% rebase("layout.tpl", title="Store App - Order Receipt")

<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 15%">
      <h4 style="text-align: center">Order #{{order_id}}</h4>
    </div>
  <div class="row">
    <div class="one-third column">
      <a class="button button-primary" href="/orders">Back to Orders</a>
    </div>
    <div class="one-third column">
      <a class="button button-primary" href="/">Return to Home</a>
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
          <th>Quantity</th>
          <th>Price</th>
          <th>Cost</th>
        </tr>
      </thead>
      <tbody style='font-weight: 300'>
        %for i in range(0, len(table)):
        <tr>
          %for j in range(0, len(table[i])):
            <td>{{'$' if j == 2 or j == 3 else ''}}{{table[i][j]}}</td>
          %end
        </tr>
        %end
      </tbody>
    </table>
  </div>
</div>
