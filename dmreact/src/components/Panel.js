import React from 'react';
import TableInputs from './Table.input';

function addRow(e) {
  return;
}

function Panel() {
  return (
    <div className="Panel">
        <form>
          <input type="number" placeholder={'Add minimum SUPPORT value'}></input>
          <input type="number" placeholder={'Add minimum CONFIDENCE value'}></input>
          <input type="button" value="Add Data"></input>
          <input type="submit"></input>
          <TableInputs/>
        </form>
    </div>
  );
}

export default Panel;
