const { createLogger, format, transports } = require('winston');

const logger = createLogger({
  level: 'info',
  format: format.combine(
    format.timestamp(),
    format.json()
  ),
  transports: [
    new transports.File({ filename: 'parser.log', handleExceptions: true }),
    new transports.Console({ handleExceptions: true })
  ]
});

const parseData = (data) => {
  try {
    const parsedData = JSON.parse(data);
    return { status: 200, message: 'Data parsed successfully', data: parsedData };
  } catch (error) {
    logger.error(`Error parsing data: ${error.message}`);
    return { status: 400, message: 'Failed to parse data' };
  }
};

module.exports = parseData;