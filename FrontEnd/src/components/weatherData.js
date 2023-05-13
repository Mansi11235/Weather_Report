
import {useState, useEffect} from 'react';
import axios from 'axios';
import Table from 'react-bootstrap/Table';
import ReactPaginate from 'react-paginate';

export default function WeatherData({stateCode, date}){
	const [data, setData] = useState([]);
	const [itemOffset, setItemOffset] = useState(0);
	const itemsPerPage = 10;
	
	const endOffset = itemOffset + itemsPerPage;
	console.log(`Loading items from ${itemOffset} to ${endOffset}`);
	
	const pageCount = Math.ceil(data.length / itemsPerPage);

	const handlePageClick = (event) => {
		const newOffset = (event.selected * itemsPerPage) % data.length;
		console.log(
		  `User requested page number ${event.selected}, which is offset ${newOffset}`
		);
		setItemOffset(newOffset);
	  };

	useEffect(() => {
		let url = 'http://127.0.0.1:8000/api/weather';
		let params = {};
		let result;

		if(date !== undefined){
			params.date = date;
		}
		if(stateCode !== undefined){
			params.state_code = stateCode;
		}
		if(params !== undefined){
			if(params.date === "")
				delete params.date;
			if(params.state_code === "")
				delete params.state_code;
			if(Object.keys(params).length !== 0)
				url += '?' + ( new URLSearchParams( params ) ).toString();
		}

		axios.get(url)
		.then(res => {
			result = res.data;
			setData(result)
		})
		.catch(err => {})

		
	}, [date, stateCode, itemOffset, endOffset])

	const currentItems = data.slice(itemOffset, endOffset);

	const output = currentItems.map((row, index) => {
		return (
			<tr className='post-card' key={index}>
				<td>{row.date}</td>
				<td>{row.maximum_temp}</td>
				<td>{row.minimum_temp}</td>
				<td>{row.precipitation}</td>
				<td>{row.state_code}</td>
			</tr>
		);
	});

	return (
		<>
			<div>
				<div >
					<div >
						<Table striped bordered hover>
							<thead>
								<tr>
									<th>Date</th>
									<th>minimum temperature</th>
									<th>maximum temperature</th>
									<th>amount of precipitation</th>
									<th>state code</th>
								</tr>
							</thead>
							<tbody>
								{output}
							</tbody>
						</Table>
					</div>
				</div>
			</div>
			<ReactPaginate
				breakLabel="..."
				nextLabel="next >"
				onPageChange={handlePageClick}
				pageRangeDisplayed={5}
				pageCount={pageCount}
				previousLabel="< previous"
				renderOnZeroPageCount={null}
				containerClassName="pagination justify-content-center"
				pageClassName="page-item"
				pageLinkClassName="page-link"
				previousClassName="page-item"
				previousLinkClassName="page-link"
				nextClassName="page-item"
				nextLinkClassName="page-link"
				activeClassName="active"
			/>
 		</>
	);
}