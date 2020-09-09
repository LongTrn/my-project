import React from 'react';

function addRow(e) {
        
}

function Panel() {
  return (
    <div className="Panel">
        <form>
            <input type="number" placeholder={'Add minimum SUPPORT value'}></input>
            <input type="number" placeholder={'Add minimum CONFIDENCE value'}></input>
            <input type="button" onClick={addRow}>Add Data</input>
            <input type="submit"></input>
        </form>
    </div>
  );
}

export default Panel;
